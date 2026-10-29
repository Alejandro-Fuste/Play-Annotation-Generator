# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_198`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_198/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 374 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 374 as fallback play end.
> - Action 'Action_PreSnap' range [0-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-345] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-355] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-371] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-81] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-336] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-365] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-319] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-332] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-92] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-334] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-339] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-316] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-365] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-374] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-275] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-116] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-355] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-228] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-284] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-350] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-358] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-337] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-345] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-374] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-93] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-82] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-307] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-325] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-330] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-339] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-351] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-361] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-295] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-370] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-275] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [308-309] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-279] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-289] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-318] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-336] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-360] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-355] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-369] for track '29' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.