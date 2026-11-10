# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_62`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [123-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-171] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-145] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-75] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-82] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-153] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-115] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-145] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-86] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-166] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [73-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-197] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-207] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-158] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-61] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-131] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-147] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-194] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-210] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.