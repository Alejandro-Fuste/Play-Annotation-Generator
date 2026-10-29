# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_134`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_134/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 115 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 418 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
> - Segment 'Action_ComboBlock' for track '15' has invalid range: start=291, end=281. Clamping end to start.
> - Action 'Action_PreSnap' range [0-27] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-104] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-317] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-373] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-386] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-288] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-370] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-318] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-344] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-415] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-356] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-281] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-293] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-335] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-351] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-370] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-302] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-325] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [291-304] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [307-308] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-317] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-345] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [354-373] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [291-311] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-330] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-352] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-372] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-406] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-282] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-335] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-339] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-356] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-405] for track '13' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-258] for track '14' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-342] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-411] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-416] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-281] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-387] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-165] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-111] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-169] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-186] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-200] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-214] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-223] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-230] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-264] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [265-270] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [283-284] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [291-302] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-161] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-170] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-306] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-168] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-364] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-370] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-375] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-401] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-336] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-399] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-272] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-325] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-378] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-282] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-315] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-322] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-394] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-400] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-418] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-376] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-408] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-333] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-378] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-383] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-403] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-384] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-415] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-414] for track '32' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.