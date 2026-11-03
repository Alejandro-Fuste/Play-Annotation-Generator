# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_41`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 48 |
| Player Tracks | 48 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 197 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [4–18], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=19.
> - Action 'Action_RunGoRoute' range [95-277] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-248] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-85] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-231] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-199] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-118] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-214] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-267] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-288] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-44] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-142] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-208] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-241] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-271] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-185] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-223] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-264] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-274] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-290] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-134] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-194] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-249] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-37] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-255] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-64] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-169] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-42] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-65] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-118] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [130-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-167] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [170-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-34] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [39-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-46] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-107] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [7-246] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [59-128] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-159] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-245] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-292] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-214] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-244] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-254] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-265] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-178] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-235] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-200] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-232] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-184] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-205] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-275] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-295] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-207] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-246] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-220] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-299] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-299] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-245] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-232] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-243] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-266] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-299] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-288] for track '39' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-299] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-265] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-299] for track '45' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '47' has 1 frames without a visible bounding box.
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
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.