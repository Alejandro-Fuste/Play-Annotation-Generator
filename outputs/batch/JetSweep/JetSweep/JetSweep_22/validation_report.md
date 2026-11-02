# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `JetSweep_22`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_BallSnap' at frame 15 targets track ID '[?]', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_ZoneBlock' range [22-68] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-73] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-161] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-236] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-193] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-218] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [0-35] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [37-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-23] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-27] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-15] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [24-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [34-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [44-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-124] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-159] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-218] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-71] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-144] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-125] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-177] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-191] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-205] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-153] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-156] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-170] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-177] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-169] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-163] for track '30' has 1 frames without a visible bounding box.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.