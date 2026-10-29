# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_214`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_214/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-39] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-86] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-99] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-60] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-87] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [37-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [48-49] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-91] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-114] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [37-57] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [58-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-18] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-65] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-91] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-72] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-125] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-63] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-74] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-125] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-104] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-109] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-125] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.