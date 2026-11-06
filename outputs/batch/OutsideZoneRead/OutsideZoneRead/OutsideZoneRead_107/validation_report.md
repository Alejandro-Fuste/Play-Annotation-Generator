# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_107`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_107/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [9–25], lower_priority='Action_ZoneBlock' annotated_start=12, effective_Action_ZoneBlock_start=26.
> - Action 'Action_None' range [9-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-85] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-95] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-63] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [9-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [9-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-43] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-68] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [58-88] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [91-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [107-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [149-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-150] for track '24' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.