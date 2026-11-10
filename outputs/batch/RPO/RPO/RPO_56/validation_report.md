# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `RPO_56`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - RPO Run Block requires exactly five verified OL positions ['C', 'LG', 'LT', 'RG', 'RT']; found ['LG', 'LT', 'RG', 'RT'].

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-112] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-122] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-139] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-110] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-113] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-109] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-94] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-135] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-112] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-180] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '25' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.