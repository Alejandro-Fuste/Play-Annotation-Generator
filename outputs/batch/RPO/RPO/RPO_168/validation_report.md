# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_168`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_168/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
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
> - Action 'Action_None' range [34-47] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-41] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-143] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-36] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-54] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-98] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-164] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-180] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-174] for track '26' has 2 frames without a visible bounding box.
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
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.