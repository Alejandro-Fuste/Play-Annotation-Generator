# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_246`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_246/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [93-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-116] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-108] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-118] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [93-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '21' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.