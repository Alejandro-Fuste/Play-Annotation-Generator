# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_96`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_96/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [66-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-152] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-224] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-77] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-104] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-228] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-192] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-209] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-222] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-181] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-217] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-217] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.