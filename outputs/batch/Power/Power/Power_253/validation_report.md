# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_253`
- **Input XML**: `outputs/batch/Power/Power/Power_253/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [7-72] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-139] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-76] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-111] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-126] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-133] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-94] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-111] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [52-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-136] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-111] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-145] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-51] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [52-74] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-51] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [53-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [82-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-74] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-107] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-98] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-111] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-126] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-111] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-128] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '31' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.