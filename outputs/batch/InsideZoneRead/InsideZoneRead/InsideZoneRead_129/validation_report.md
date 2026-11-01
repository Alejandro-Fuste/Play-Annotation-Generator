# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_129`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [21–33], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=34.
> - Action 'Action_None' range [21-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-200] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-44] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-87] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-202] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [21-27] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-182] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-44] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-79] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-44] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-182] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-194] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [47-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-55] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [56-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [105-156] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [158-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [161-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [166-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-200] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-112] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-139] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-74] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-210] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-88] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-71] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-96] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-198] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-189] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-139] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '33' has 2 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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