# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_104`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_104/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Overlapping action conflict at frame 155 for track '11': 'Action_ZoneBlock' vs 'Action_PressEdge'. Overriding with 'Action_PressEdge'.
> - Action 'Action_PreSnap' range [0-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-207] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-402] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-412] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-417] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-246] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-251] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-419] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-224] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-390] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-183] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-419] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-305] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-419] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-322] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [155-158] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-373] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [375-380] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-386] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-194] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-405] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-211] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-228] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-363] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-304] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-312] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-331] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-60] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-298] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-302] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-307] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 171, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [171-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-163] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-234] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-241] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-361] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [160-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-277] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-182] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-235] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-408] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-308] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-419] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-246] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-267] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-405] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-261] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-282] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-299] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-296] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-300] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-387] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-344] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-408] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-413] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-408] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [410-411] for track '31' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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