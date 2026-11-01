# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_68`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_68/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [36–49], lower_priority='Action_ZoneBlock' annotated_start=39, effective_Action_ZoneBlock_start=50.
> - Action 'Action_None' range [36-77] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-191] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-237] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-251] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-66] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-94] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-133] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-209] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [211-219] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-57] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-68] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-248] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-86] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-130] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [68-78] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [85-92] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [98-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-269] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [69-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-92] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-105] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [36-47] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-184] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-90] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-183] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [36-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-108] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-152] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-232] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-246] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-269] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-178] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-212] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-242] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-178] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-225] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-245] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-222] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-252] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-209] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '34' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.