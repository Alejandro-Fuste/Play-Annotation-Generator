# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_367`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_367/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 733: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [13–27], lower_priority='Action_ZoneBlock' annotated_start=16, effective_Action_ZoneBlock_start=28.
> - Action 'Action_None' range [13-39] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-245] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-136] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-145] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-245] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-229] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-77] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-259] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-259] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-64] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-243] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '25' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.