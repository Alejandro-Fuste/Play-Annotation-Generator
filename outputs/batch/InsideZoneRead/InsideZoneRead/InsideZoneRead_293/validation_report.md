# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_293`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_293/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 141 frames exceeds threshold 90 frames [start=6, end=146].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 141 frames exceeds threshold 90 frames [start=6, end=146].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 141 frames exceeds threshold 90 frames [start=6, end=146].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 141 frames exceeds threshold 90 frames [start=6, end=146].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [3–14], lower_priority='Action_ZoneBlock' annotated_start=6, effective_Action_ZoneBlock_start=15.
> - Action 'Action_None' range [3-103] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-160] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-94] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-108] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-59] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-189] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [50-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [170-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-27] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-201] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-108] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-186] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-62] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-146] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [6-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [131-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [15-27] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-79] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-163] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-190] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-200] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-189] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '33' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.