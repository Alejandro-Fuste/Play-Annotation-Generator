# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_150`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_150/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-309] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-359] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-155] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-348] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-354] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-123] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-164] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-340] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-246] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-321] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-240] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-321] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-359] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-256] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-205] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-357] for track '23' has 1 frames without a visible bounding box.
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