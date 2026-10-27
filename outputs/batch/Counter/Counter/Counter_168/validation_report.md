# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Counter_168`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_168/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 66 |
| Player Tracks | 66 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 180 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 839 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BallCarry' at frame 82 targets track ID '?', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 338: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 839 as fallback play end.
> - Segment 'Action_BallSnap' for track '8' has invalid range: start=89, end=54. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '11' has invalid range: start=89, end=54. Clamping end to start.
> - Segment 'Action_PullBlock' for track '12' has invalid range: start=89, end=63. Clamping end to start.
> - Action 'Action_None' range [37-43] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-54] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-552] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-534] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-386] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [388-468] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [478-552] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-446] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-468] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-552] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-459] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-552] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-552] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-276] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-289] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-264] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-277] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-289] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-302] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-314] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-391] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-410] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [413-477] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [484-485] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-552] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-250] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-287] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [365-385] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-393] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-552] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [89-299] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [324-329] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-303] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-345] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-406] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-169] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [171-278] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-250] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-269] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-294] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-345] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-371] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-393] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [395-411] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-552] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-552] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-140] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-295] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-345] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-552] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-255] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-300] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [324-343] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-383] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-140] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-277] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-287] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-312] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [316-343] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-552] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [89-101] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-115] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-138] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-300] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-309] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-389] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-277] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-305] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-540] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-552] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-351] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-374] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [394-552] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-422] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [427-431] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [436-519] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [530-552] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-339] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-350] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-552] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [362-552] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [580-794] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [403-411] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [413-549] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [428-430] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-434] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-452] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-458] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [506-508] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-512] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [514-552] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [517-520] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [523-552] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [538-540] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-552] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [551-552] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-771] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [580-839] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [580-749] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-738] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [741-796] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-684] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-703] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-697] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [700-713] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [580-734] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [736-737] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [756-791] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-695] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-693] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [696-765] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [580-628] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [630-674] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [685-711] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [714-800] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-589] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-602] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [604-694] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-639] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [641-643] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [657-660] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [665-666] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [669-670] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [672-684] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [690-707] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [709-711] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [719-720] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [723-822] for track '52' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [600-647] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [678-716] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [721-764] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [709-825] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [711-722] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [725-815] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [729-764] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [770-802] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [738-828] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [835-836] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [741-788] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [756-759] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [761-784] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [763-768] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [765-791] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [794-826] for track '62' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [830-835] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [768-787] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [782-786] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [787-790] for track '65' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.