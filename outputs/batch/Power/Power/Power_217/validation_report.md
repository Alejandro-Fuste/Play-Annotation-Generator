# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_217`
- **Input XML**: `outputs/batch/Power/Power/Power_217/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 45 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [8-126] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-47] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-235] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-235] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-237] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-15] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-183] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-90] for track '21' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.