# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_6`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [177–191], lower_priority='Action_ZoneBlock' annotated_start=180, effective_Action_ZoneBlock_start=192.
> - Action 'Action_None' range [177-259] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-254] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [186-190] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-288] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-262] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-345] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [199-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-278] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-246] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-440] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [218-252] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [254-263] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [193-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [210-213] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [228-232] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-246] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [259-264] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-280] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [216-224] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [228-240] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [242-250] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-259] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-184] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-195] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-223] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-252] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-265] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [188-193] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-26] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-110] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-136] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-161] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-434] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-228] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-350] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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