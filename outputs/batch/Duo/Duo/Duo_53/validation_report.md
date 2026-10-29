# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_53`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Action 'Action_PreSnap' range [0-244] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-311] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-353] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-334] for track '3' has 8 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-338] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-358] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-339] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-303] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-347] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-240] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [241-258] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [267-275] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [277-278] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [286-288] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-351] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-262] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-358] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-316] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-49] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [241-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-310] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-175] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-241] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-268] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-15] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-325] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-62] for track '21' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-356] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-332] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-346] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-42] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-70] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-323] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-357] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-278] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-290] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-349] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-358] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-332] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-342] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-358] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-336] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-353] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-357] for track '33' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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