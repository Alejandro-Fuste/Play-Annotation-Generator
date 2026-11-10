# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_129`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_129/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [60-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-175] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-138] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-131] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-104] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-161] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-149] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-85] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-79] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-91] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '30' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.