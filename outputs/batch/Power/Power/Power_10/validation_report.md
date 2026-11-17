# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_10`
- **Input XML**: `outputs/batch/Power/Power/Power_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [15-112] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-123] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-218] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-223] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-102] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-58] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-115] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-229] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-92] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-233] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-178] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-158] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-160] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.