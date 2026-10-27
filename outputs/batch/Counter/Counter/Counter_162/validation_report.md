# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_162`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_162/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '20' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [121-123] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-81] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-88] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [40-82] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [84-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-221] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [37-57] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-73] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-169] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [31-113] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.