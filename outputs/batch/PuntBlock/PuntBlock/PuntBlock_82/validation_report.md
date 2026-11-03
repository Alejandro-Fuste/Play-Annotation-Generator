# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_82`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-280] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-321] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-350] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-86] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-107] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-122] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-294] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-243] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-248] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-318] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-389] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [50-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [84-93] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-242] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-254] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-320] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-389] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-83] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-232] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-328] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-365] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-381] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-152] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-331] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-385] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-119] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-124] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-8] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-369] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-292] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-388] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-375] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-171] for track '24' has 9 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-179] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-211] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-195] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-335] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-351] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-183] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-318] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-389] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-151] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-187] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-228] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-234] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-305] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-382] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-389] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-270] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-342] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-289] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-294] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-299] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-274] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-287] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-329] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-334] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-342] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-281] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-295] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-384] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-363] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-378] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-339] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-343] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-365] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-372] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-389] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-358] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-365] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-389] for track '43' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.