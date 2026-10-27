# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_179`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_179/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [33-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-157] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-218] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [33-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-212] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-227] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-222] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-226] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-230] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-221] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [36-77] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-106] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-120] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-235] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [40-63] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [36-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-102] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-14] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-169] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-233] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-229] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-162] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [157-177] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '29' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.