# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_35`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 175 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [210–224], lower_priority='Action_ZoneBlock' annotated_start=213, effective_Action_ZoneBlock_start=225.
> - Segment 'Action_BallCarry' for track '16' has invalid range: start=257, end=247. Clamping end to start.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 93 frames exceeds threshold 90 frames [start=213, end=305].
> - Action 'Action_None' range [210-354] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [210-236] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-266] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-277] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-253] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-281] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-250] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-282] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-286] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-297] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-350] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [358-364] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-372] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-421] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [425-430] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-445] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [210-249] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-287] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-410] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [414-415] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [423-427] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [225-231] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [233-235] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [240-251] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [255-277] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-284] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-236] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [238-251] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [256-266] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [270-281] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [210-270] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-277] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [221-244] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [292-305] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 306, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [306-306] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-340] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [358-427] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-313] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-339] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-381] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [387-449] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [257-362] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-242] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-247] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-235] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [238-249] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-250] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [253-288] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [292-305] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-449] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [213-234] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [238-251] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [255-262] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [274-282] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-236] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-251] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-289] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-317] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [319-350] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-266] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-282] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-340] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-372] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-379] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-418] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [425-427] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-445] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-270] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-277] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-266] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-282] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-341] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-350] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-372] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-382] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-418] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [420-446] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-338] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [372-383] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-418] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [423-427] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-436] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-440] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [320-344] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-365] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [370-372] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-396] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-399] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [426-427] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-449] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-344] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-341] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-350] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [357-362] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-382] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-394] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-422] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [425-437] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [441-445] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-344] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-360] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-380] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-389] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-449] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [345-346] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-395] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [399-400] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-403] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-419] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [425-426] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-438] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-443] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-361] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-381] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-420] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [423-449] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-381] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-393] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [395-421] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [385-398] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-442] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [442-443] for track '41' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.