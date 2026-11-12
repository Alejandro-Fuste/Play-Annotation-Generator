# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_91`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_91/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [106–118], lower_priority='Action_ZoneBlock' annotated_start=109, effective_Action_ZoneBlock_start=119.
> - Action 'Action_None' range [106-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-182] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-136] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-149] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-153] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-239] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [136-137] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-155] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-236] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-136] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-227] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '25' has 1 frames without a visible bounding box.
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