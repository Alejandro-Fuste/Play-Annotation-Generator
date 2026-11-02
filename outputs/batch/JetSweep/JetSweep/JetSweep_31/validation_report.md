# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_31`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 28 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [48–61], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=62.
> - Action 'Action_None' range [48-133] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-197] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-95] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-189] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-85] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-115] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-175] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-220] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [75-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-169] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '31' has 1 frames without a visible bounding box.
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