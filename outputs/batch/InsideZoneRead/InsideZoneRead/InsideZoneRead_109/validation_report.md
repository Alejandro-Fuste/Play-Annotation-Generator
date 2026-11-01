# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_109`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 219: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [94–110], lower_priority='Action_ZoneBlock' annotated_start=97, effective_Action_ZoneBlock_start=111.
> - Action 'Action_None' range [94-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-255] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-264] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [129-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-153] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-181] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-196] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-221] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-190] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-196] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-164] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-189] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-265] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [94-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-235] for track '22' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.