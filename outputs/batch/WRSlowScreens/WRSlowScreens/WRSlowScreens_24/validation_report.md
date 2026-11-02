# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_24`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 37 |
| Ball Tracks | 1 |
| CSV events parsed | 20 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [2–17], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=18.
> - Action 'Action_None' range [2-308] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-368] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-62] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-42] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-89] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-363] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [385-386] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-23] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [88-232] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [246-346] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [377-382] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-159] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-218] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-242] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-44] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-228] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [230-267] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [274-300] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [303-330] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-33] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-317] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [321-374] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [384-387] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-14] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-16] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-23] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-37] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-265] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [136-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [242-248] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [264-290] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-268] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-341] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-352] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-385] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-218] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-243] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-213] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-245] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-308] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-295] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-314] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-419] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-386] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-393] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-415] for track '37' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.