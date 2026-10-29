# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_206`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_206/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-125] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-82] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-110] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-125] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [45-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-83] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [48-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [60-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-63] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-91] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' for track '20' starts at frame 45, but the player has no visible bounding box on this frame.
> - Action 'Action_ComboBlock' range [45-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [59-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-76] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-122] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-75] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-85] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-92] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-115] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-125] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.