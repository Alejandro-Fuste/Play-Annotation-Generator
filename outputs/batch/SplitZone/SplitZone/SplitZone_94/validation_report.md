# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_94`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_94/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [105–110], lower_priority='Action_ZoneBlock' annotated_start=108, effective_Action_ZoneBlock_start=111.
> - Action 'Action_None' range [105-217] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-203] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-143] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [150-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [164-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-170] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-127] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-170] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-183] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-174] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-234] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-194] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [134-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-126] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [158-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-232] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [105-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [108-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-217] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-196] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-139] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-128] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-239] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-222] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-235] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-221] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-230] for track '22' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.