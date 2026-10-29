# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_86`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_86/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-167] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-99] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-113] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-152] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-179] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-123] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-143] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [72-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [92-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-115] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-146] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-179] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '29' has 1 frames without a visible bounding box.
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