# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_209`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_209/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [57–71], lower_priority='Action_ZoneBlock' annotated_start=58, effective_Action_ZoneBlock_start=72.
> - Action 'Action_None' range [57-240] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [58-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-279] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-296] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-241] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-234] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-252] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-226] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-238] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-176] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-238] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 57, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [57-61] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-244] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-214] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-218] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-155] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-198] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-208] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-218] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-226] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-264] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-277] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '37' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.