# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_4`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [37-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [38-64] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [77-84] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [38-69] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [38-43] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [48-52] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [61-63] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [67-72] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [38-41] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-72] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [78-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-127] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PullBall' range [57-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [88-131] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PullBall' range [136-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-97] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-141] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-158] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-97] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-83] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-89] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-209] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-140] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-155] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-191] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-164] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-165] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [167-187] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-191] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '34' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.