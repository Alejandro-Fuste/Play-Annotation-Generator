# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_35`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
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
> - Action 'Action_PullBall' range [51-52] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-44] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-111] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-67] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-59] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-80] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-37] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-65] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-82] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-88] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-178] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-159] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '29' has 1 frames without a visible bounding box.
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