# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_47`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [61–76], lower_priority='Action_PassBlock' annotated_start=64, effective_Action_PassBlock_start=77.
> - Action 'Action_None' range [61-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-164] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-284] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-290] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-158] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-186] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-200] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-317] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-311] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [313-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-106] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-156] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [158-167] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-301] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-329] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-293] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-311] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-315] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-300] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-156] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-286] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-313] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-326] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-281] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-258] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-316] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [321-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-286] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-311] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '28' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.