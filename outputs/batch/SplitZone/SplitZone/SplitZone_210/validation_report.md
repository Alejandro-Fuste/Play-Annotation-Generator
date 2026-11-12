# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_210`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_210/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 152 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 779 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 779 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (LG) duration 205 frames exceeds threshold 90 frames [start=426, end=630].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (RT) duration 276 frames exceeds threshold 90 frames [start=426, end=701].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 276 frames exceeds threshold 90 frames [start=426, end=701].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [423–431], lower_priority='Action_ZoneBlock' annotated_start=426, effective_Action_ZoneBlock_start=432.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 276 frames exceeds threshold 90 frames [start=426, end=701].
> - Action 'Action_None' range [423-647] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [651-690] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [700-719] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-212] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-293] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-349] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-419] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-480] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [494-691] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [693-732] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-134] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-660] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [700-702] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-133] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-38] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [432-665] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-619] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [625-706] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [710-739] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [744-758] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-94] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [426-550] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [552-630] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-196] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [462-482] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [486-488] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [492-642] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [647-672] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [696-765] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [773-774] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-251] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-290] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-364] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-393] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-408] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-425] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [457-459] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [485-588] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [592-603] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [607-674] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [678-680] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [702-703] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-422] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-598] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [605-672] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-422] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-593] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-347] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-385] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-434] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-634] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [657-688] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [697-779] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-422] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [432-579] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [581-658] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [663-670] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [672-701] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [702-720] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [725-728] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-636] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [641-651] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [655-707] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-212] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-417] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [462-469] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-515] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-578] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [426-547] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [551-694] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-563] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [570-574] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [578-586] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [589-595] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [599-601] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [604-616] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [618-629] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [597-608] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-649] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [678-705] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [617-618] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [635-680] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [683-751] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [650-653] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [685-694] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [670-697] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [706-709] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [711-716] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [725-742] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [744-745] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [748-754] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [761-773] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [671-678] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [673-698] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [682-714] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [728-777] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [687-694] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [697-706] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [753-754] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [715-774] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [717-720] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [717-751] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [721-722] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [723-725] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [748-759] for track '40' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.