# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_42`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_42/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [38–52], lower_priority='Action_PassBlock' annotated_start=41, effective_Action_PassBlock_start=53.
> - Action 'Action_None' range [38-116] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 118, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [118-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-147] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-185] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [135-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [143-182] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [209-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-234] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-94] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-182] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-105] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-47] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-7] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 38, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [38-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-60] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [69-71] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-98] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 118, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [118-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-190] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-93] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-203] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-224] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-216] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '30' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.