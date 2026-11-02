# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_55`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [34–45], lower_priority='Action_ZoneBlock' annotated_start=36, effective_Action_ZoneBlock_start=46.
> - Action 'Action_None' range [34-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-113] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [36-73] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-145] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [36-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-196] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-101] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 95, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [95-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [36-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-13] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-207] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-7] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [63-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.