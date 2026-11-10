# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_252`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_252/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 24 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
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
> - Action 'Action_None' range [51-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-112] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-114] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-109] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-171] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-99] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-127] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-85] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-180] for track '24' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.