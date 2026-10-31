# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_58`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_58/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [5–20], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=21.
> - Action 'Action_PassBlock' range [8-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-205] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-237] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [134-220] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [222-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-213] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-59] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-73] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-119] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-191] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-165] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '30' has 1 frames without a visible bounding box.
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