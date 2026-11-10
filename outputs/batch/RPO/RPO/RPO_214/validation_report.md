# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_214`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_214/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [59-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-153] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 59, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [59-59] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-127] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-123] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-187] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-234] for track '23' has 1 frames without a visible bounding box.
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
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.