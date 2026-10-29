# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_219`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_219/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-4] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [45-71] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [74-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-125] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-41] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-81] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-125] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-29] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [54-73] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [45-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [78-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-125] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [45-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-125] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [45-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-113] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-125] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-34] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-40] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-97] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-116] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-39] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-17] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-45] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-76] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-122] for track '25' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-57] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-101] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-113] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-64] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-72] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-76] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-86] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-106] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-113] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-125] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-123] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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