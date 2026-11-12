# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_158`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_158/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 36 |
| Ball Tracks | 1 |
| CSV events parsed | 22 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RT) duration 177 frames exceeds threshold 90 frames [start=87, end=263].
> - Validation warning: Action 'Action_BlockSecondLevel' for track '5' (C) duration 160 frames exceeds threshold 90 frames [start=104, end=263].
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [84–89], lower_priority='Action_ZoneBlock' annotated_start=87, effective_Action_ZoneBlock_start=90.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RG) duration 177 frames exceeds threshold 90 frames [start=87, end=263].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (LT) duration 177 frames exceeds threshold 90 frames [start=87, end=263].
> - Action 'Action_BallCarry' range [120-325] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-259] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-282] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-344] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-357] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-126] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-324] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-146] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-291] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-338] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-359] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-65] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-351] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [85-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-96] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-344] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-356] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-326] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-354] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-320] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-331] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-359] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [145-359] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-359] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-252] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-260] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-359] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-238] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-308] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-340] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-216] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-262] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-277] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-288] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-299] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-320] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-324] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-332] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-344] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-334] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [348-353] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-357] for track '36' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.