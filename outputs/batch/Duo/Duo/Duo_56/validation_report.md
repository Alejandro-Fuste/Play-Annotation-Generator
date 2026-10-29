# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_56`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Deduplicated duplicate event 'Action_ComboBlock' at frame 87 for track '5'.
> - Action 'Action_PreSnap' range [0-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-179] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [87-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-162] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-150] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-129] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-161] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [87-133] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-162] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-179] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [87-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [105-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [120-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-136] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-144] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-179] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.