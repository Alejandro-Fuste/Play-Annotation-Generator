# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_61`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_61/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 170 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [41–54], lower_priority='Action_ZoneBlock' annotated_start=44, effective_Action_ZoneBlock_start=55.
> - Action 'Action_None' range [41-135] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-171] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-219] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [223-233] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-120] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-60] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-326] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-337] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-159] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-200] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-312] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-340] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-105] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-186] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-236] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-156] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-331] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [334-337] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-344] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-160] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-359] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-272] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-198] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [71-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-174] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-188] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-59] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-68] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-72] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-330] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-339] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-206] for track '20' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-225] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-240] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-308] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-313] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-346] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-114] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-257] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-263] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-301] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-343] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-94] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-196] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-206] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-234] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [237-260] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-287] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-349] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-182] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-190] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-206] for track '29' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-233] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [235-254] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [256-287] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [289-329] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-338] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-254] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-294] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-308] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-359] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-278] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [258-359] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-307] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-313] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [315-322] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-337] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-343] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-318] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-339] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-336] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-342] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '45' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.