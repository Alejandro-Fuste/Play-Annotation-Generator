# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_3`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [48-234] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-70] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-142] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-121] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [56-128] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [131-138] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-239] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PullBall' range [70-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [49-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '21' starts at frame 96, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [96-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-109] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '26' has 1 frames without a visible bounding box.
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