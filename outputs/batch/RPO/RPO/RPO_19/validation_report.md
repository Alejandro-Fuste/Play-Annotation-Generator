# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_19`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_19/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [104-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-135] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [59-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-70] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-269] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-231] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-233] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-74] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-17] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-39] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-58] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 59, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [59-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-105] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-261] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-268] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-219] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-244] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-172] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-256] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-225] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-194] for track '26' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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