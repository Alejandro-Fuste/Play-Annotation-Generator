# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_85`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_85/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [116–131], lower_priority='Action_ZoneBlock' annotated_start=123, effective_Action_ZoneBlock_start=132.
> - Action 'Action_None' range [116-204] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [173-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-151] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-256] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-152] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-169] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [116-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-193] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-184] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-201] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-153] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-269] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-217] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-252] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.