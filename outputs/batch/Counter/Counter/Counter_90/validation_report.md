# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_90`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_90/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [77–95], lower_priority='Action_DownBlock' annotated_start=79, effective_Action_DownBlock_start=96.
> - Action 'Action_None' range [77-162] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [79-94] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [106-109] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [81-156] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [159-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [131-223] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [232-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-142] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [109-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-253] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-274] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-279] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-297] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [96-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-143] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-198] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [79-109] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-126] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [79-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [136-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-119] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-169] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-246] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-170] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-251] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-281] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-271] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-287] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.