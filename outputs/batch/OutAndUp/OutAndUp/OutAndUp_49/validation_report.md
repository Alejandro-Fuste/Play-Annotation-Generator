# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_49`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 52: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_SellOut' range [78-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [107-245] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-245] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-223] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-50] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-63] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-92] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-54] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-171] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-22] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-182] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-39] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-91] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-104] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-202] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-172] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-244] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-244] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '31' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.