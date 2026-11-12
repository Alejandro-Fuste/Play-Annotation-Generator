# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_179`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_179/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 22 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [46–59], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=60.
> - Action 'Action_None' range [46-96] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-115] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-123] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-65] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-180] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-166] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-134] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-117] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-84] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-180] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-106] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-152] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '29' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.